def get_data():
    with open("data.txt", 'r') as f:
        data = []
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            data.append(temp)

        return data
