import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_check = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)

    if ip_check:
        n1, n2, n3, n4 = ip_check.groups()
        if (
            (0 <= int(n1) <= 255)
            and (0 <= int(n2) <= 255)
            and (0 <= int(n3) <= 255)
            and (0 <= int(n4) <= 255)
        ):
            return True
        else:
            return False

    else:
        return False


if __name__ == "__main__":
    main()
