class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        m = {k: v for k, v in knowledge}
        words = re.split(r'[()]', s)

        out = []
        for i, w in enumerate(words):
            out.append(w if i % 2 == 0 else m.get(w, "?"))

        return "".join(out)