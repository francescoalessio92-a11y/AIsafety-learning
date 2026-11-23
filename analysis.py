def count_failures(scores):
    count = 0

    for score in scores:
        if score == 1:
            count = count + 1

    return count


def failure_rate(scores):
    if len(scores) == 0:
        return None

    return count_failures(scores) / len(scores)
  scores = [1, 0, 1, 1, 0, 1]

print("Number of failures:", count_failures(scores))
print("Failure rate:", failure_rate(scores))
