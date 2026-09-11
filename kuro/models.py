"""Adapters that turn a language model into the callable `Reader` needs.

`Reader` takes any callable from prompt to text. These are the two adapters worth having: the
Anthropic API for real use, and a fixed-answer stub for tests. Neither is imported by default so
the package stays free of the dependency until it is asked for.

    from kuro.models import anthropic_model
    reader = Reader(model=anthropic_model(), known_units=corpus_units)

The API key is read from the environment (ANTHROPIC_API_KEY) and never stored here.
"""
import os


def anthropic_model(model_name='claude-sonnet-4-6', max_tokens=400, temperature=0.0):
    """A callable prompt -> text over the Anthropic Messages API.

    Temperature 0 because the task is extraction, not invention: the same passage should yield the
    same proposition every time, and a reader that varies is a reader that cannot be audited.
    """
    try:
        import anthropic
    except ImportError as e:
        raise ImportError('pip install anthropic') from e
    key = os.environ.get('ANTHROPIC_API_KEY')
    if not key:
        raise RuntimeError('set ANTHROPIC_API_KEY in the environment; it is not stored in the package')
    client = anthropic.Anthropic(api_key=key)

    def call(prompt):
        r = client.messages.create(model=model_name, max_tokens=max_tokens, temperature=temperature,
                                   messages=[{'role': 'user', 'content': prompt}])
        return ''.join(b.text for b in r.content if getattr(b, 'type', '') == 'text')
    return call


def stub_model(answers):
    """For tests: answers is a dict from a substring of the prompt to the reply, or a single reply."""
    def call(prompt):
        if isinstance(answers, str):
            return answers
        for key, reply in answers.items():
            if key in prompt:
                return reply
        return 'NONE: no rule matched'
    return call
