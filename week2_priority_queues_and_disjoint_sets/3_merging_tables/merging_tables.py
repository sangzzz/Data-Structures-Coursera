# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def find(self, i):
        if self.parents[i] == i:
            return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return True
        if self.ranks[i_id] <= self.ranks[j_id]:
            self.row_counts[j_id] += self.row_counts[i_id]
            self.parents[i_id] = j_id
            self.row_counts[i_id] = 0
            if self.ranks[i_id] == self.ranks[j_id]:
                self.ranks[j_id] += 1
        else:
            self.row_counts[i_id] += self.row_counts[j_id]
            self.parents[j_id] = i_id
            self.row_counts[j_id] = 0
        self.max_row_count = max(
            self.row_counts[i_id], self.row_counts[j_id], self.max_row_count)
        # This max step is very important in deciding the timecomplexity
        # By making sure that it is only comparing three elements at any step, we are greatly
        # reducing the time complexity

        # Took me a while to figure this out. XD

    # def merge(self, src, dst):
    #     src_parent = self.get_parent(src)
    #     dst_parent = self.get_parent(dst)

    #     if src_parent == dst_parent:
    #         return False

    #     # merge two components
    #     # use union by rank heuristic
    #     # update max_row_count with the new maximum table size
    #     return True

    # def get_parent(self, table):
    #     # find parent and compress path
    #     return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    # sol = []
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.union(dst - 1, src - 1)
        print(db.max_row_count)
        # sol.append(db.max_row_count)
    # for each in sol:
        # print(each)


if __name__ == "__main__":
    main()
