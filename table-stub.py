from opensmtpd import table

def check(token, service, key):
    #table.boolean(token, True)
    #table.boolean(token, True)
    table.failure(token)

def lookup(token, service, key):
    table.result(token, "foobar")
    #table.result(token)
    #table.failure(token)

def fetch(token, service):
    table.result(token, "foobar")
    #table.result(token)
    #table.failure(token)

def main():
    table.on_check(check)
    table.on_lookup(lookup)
    table.on_fetch(fetch)
    table.dispatch()

if __name__ == "__main__":
    main()