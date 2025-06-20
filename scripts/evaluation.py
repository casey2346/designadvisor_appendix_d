import json
import math
from collections import defaultdict


def jensen_shannon_divergence(p, q):
    def kl_divergence(p, q):
        return sum(p[i] * math.log(p[i] / q[i], 2) if p[i] != 0 else 0 for i in range(len(p)))

    m = [(pi + qi) / 2 for pi, qi in zip(p, q)]
    return 0.5 * kl_divergence(p, m) + 0.5 * kl_divergence(q, m)


def parse_jsonl(file_path):
    topic_count = defaultdict(int)
    with open(file_path, "r") as f:
        for line in f:
            entry = json.loads(line)
            agent = entry["agent"]
            for word in entry["content"].lower().split():
                topic_count[(agent, word)] += 1
    return topic_count


if __name__ == "__main__":
    import os

    file_path = os.path.join(os.path.dirname(__file__), "../logs/trackA_session1.jsonl")
    counts = parse_jsonl(file_path)

    agents = sorted(set(a for a, _ in counts))
    words = sorted(set(w for _, w in counts))
    dist = {a: [counts.get((a, w), 0) for w in words] for a in agents}
    total = {a: sum(dist[a]) for a in agents}
    probs = {a: [v / total[a] if total[a] > 0 else 0 for v in dist[a]] for a in agents}

    if len(agents) >= 2:
        d = jensen_shannon_divergence(probs[agents[0]], probs[agents[1]])
        print(f"JS Divergence between {agents[0]} and {agents[1]}: {d:.4f}")
    else:
        print("Not enough agents to compute divergence.")
