# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


def main():
    n_queries = int(input())
    queries = []
    for i in range(0, n_queries):
        queries.append(input().split())
    phonebook = {}
    for i in queries:
        op = i[0]
        num = i[1]
        if op == 'add':
            name = i[2]
            phonebook[num] = name
        elif op == 'find':
            try:
                print(phonebook[num])
            except:
                print("not found")
        else:
            try:
                del phonebook[num]
            except:
                continue


if __name__ == '__main__':
    # write_responses(process_queries(read_queries()))
    main()
