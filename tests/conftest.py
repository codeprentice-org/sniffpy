from sniffpy.mimetype import MIMEType

def pytest_assertrepr_compare(op, left, right):
    resp = None
    if isinstance(left, MIMEType) and isinstance(right, MIMEType) and \
            op == "==":
        resp = ["Comparing MIMEType instances:"]
        if left.type != right.type:
            resp.append("Type does not match: {} != {}".format(left.type, right.type))
        if left.subtype != right.subtype:
            resp.append(
                "Subtype does not match: {} != {}".format(
                    left.subtype, right.subtype))

        for key in left.parameters.keys():
            if key not in right.parameters:
                resp.append(
                    "Parameter {} in the first MIMEType not present in the second".format(key))
            else:
                if left.parameters[key] != right.parameters[key]:
                    resp.append(
                        "Parameter {} does not match: {} != {}".format(
                            key, left.parameters[key], right.parameters[key]))

        for key in right.parameters.keys():
            if key not in left.parameters:
                resp.append(
                    "Parameter {} in the second MIMEType not present in the second".format(key))
            else:
                if left.parameters[key] != right.parameters[key]:
                    resp.append(
                        "Parameter {} does not match: {} != {}".format(
                            key, left.parameters[key], right.parameters[key]))
    return resp
