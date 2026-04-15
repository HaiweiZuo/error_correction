from agents.error_correction.agent import _should_avoid_tool_strategy


class _DummyCfg:
    def __init__(self, model_name: str, base_url: str = ""):
        self._model_name = model_name
        self.base_url = base_url

    def resolve_model_name(self, model_name=None, *, use_light=False):
        return model_name or self._model_name


def test_should_avoid_tool_strategy_for_deepseek_reasoner():
    cfg = _DummyCfg(model_name="deepseek-reasoner", base_url="https://api.deepseek.com")
    assert _should_avoid_tool_strategy("openai", None, cfg) is True


def test_should_not_avoid_tool_strategy_for_deepseek_chat():
    cfg = _DummyCfg(model_name="deepseek-chat", base_url="https://api.deepseek.com")
    assert _should_avoid_tool_strategy("openai", None, cfg) is False

