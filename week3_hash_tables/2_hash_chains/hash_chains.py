# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


global T


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for i in range(0, bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = ((ans * self._multiplier + ord(c)) %
                   self._prime + self._prime) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        # print(' '.join(chain))
        for i in self.elems[chain]:
            print(i, end=' ')
        print('')

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        # if query.type == "check":
        #     # use reverse order, because we append strings to the end
        #     self.write_chain(cur for cur in reversed(self.elems)
        #                      if self._hash_func(cur) == query.ind)
        # else:
        #     try:
        #         ind = self.elems.index(query.s)
        #     except ValueError:
        #         ind = -1
        #     if query.type == 'find':
        #         self.write_search_result(ind != -1)
        #     elif query.type == 'add':
        #         if ind == -1:
        #             self.elems.append(query.s)
        #     else:
        #         if ind != -1:
        #             self.elems.pop(ind)
        if query.type == 'check':
            self.write_chain(query.ind)
        else:
            try:
                hq = self._hash_func(query.s)
                if query.type == 'find':
                    if query.s in T:
                        print('yes')
                    else:
                        print('no')
                elif query.type == 'add':
                    if query.s in T:
                        return None
                    else:
                        T[query.s] = 1
                        self.elems[hq] = [query.s] + self.elems[hq]
                else:
                    if query.s not in T:
                        return None
                    else:
                        del T[query.s]
                        self.elems[hq].pop(self.elems[hq].index(query.s))
            except:
                return None

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    T = {}
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()


# global T

# def main():
#     n = int(input())
#     q = int(input())


# if __name__ == 'main':
#     main()
