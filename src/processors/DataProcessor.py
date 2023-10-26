class DataProcessor:
    @staticmethod
    def get_time_stamps(time):
        return list(set(time.astype(int)))

    @staticmethod
    def get_avg_by_second(data, time):
        time_stamps = DataProcessor.get_time_stamps(time)
        average = []
        sum = 0

        for (previous_time, current_time, value) in zip(time_stamps, time_stamps[1:], data):
            sum += value
            if current_time != previous_time:
                average.append(sum)
                sum = 0

        return average

    @staticmethod
    def get_throughput(data, time):
        time_stamps = DataProcessor.get_time_stamps(time)
        throughput = []
        sum = 0

        for (previous_time, current_time, value) in zip(time_stamps, time_stamps[1:], data):
            sum += value
            if current_time != previous_time:
                throughput.append(sum * (1024 ** 2) / 1e6)
                sum = 0

        return throughput
