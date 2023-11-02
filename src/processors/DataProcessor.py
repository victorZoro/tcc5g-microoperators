class DataProcessor:
    @staticmethod
    def get_transformed_xml(xml_document):
        """
        Transforms a XML document into a dictionary and returns it.

        yield gives a return, but it doesn't stop the method.

        Solution by Epython Lab in YouTube video https://www.youtube.com/watch?v=GFpBYaTJ1uQ

        Args:
            xml_document (etree.ElementTree): XML document.

        Returns:
            element: Dictionary with the XML document.
        """

        attribute = xml_document.attrib

        for xml in xml_document.iter('Flow'):
            element = attribute.copy()
            element.update(xml.attrib)
            yield element

    @staticmethod
    def get_time_stamps(time):
        if isinstance(time, list):
            for index, value in enumerate(time):
                time[index] = int(value)
            return time

        return time.astype(int)

    @staticmethod
    def get_average(data):
        return sum(data) / len(data)

    @staticmethod
    def get_avg_by_second(data, time, scale=1):
        time_stamps = DataProcessor.get_time_stamps(time)
        average = []
        aux = []

        for (previous_time, current_Time, value) in zip(time_stamps, time_stamps[1:], data):
            aux.append(value)
            if current_Time != previous_time:
                average.append(DataProcessor.get_average(aux) * scale)
                aux = []

        return average

    @staticmethod
    def get_jitter(data, time):
        time_stamps = DataProcessor.get_time_stamps(time)
        jitter = []
        aux = []

        for (previous_time, current_time, value, next_value) in zip(time_stamps, time_stamps[1:], data, data[1:]):
            aux.append(next_value - value)

            if current_time != previous_time:
                jitter.append(DataProcessor.get_average(aux) * 1e3)
                aux = []

        return jitter

    @staticmethod
    def get_throughput(data, time):
        time_stamps = DataProcessor.get_time_stamps(time)
        throughput = []
        aux = []

        for (previous_time, current_time, value) in zip(time_stamps, time_stamps[1:], data):
            aux.append(value)
            if current_time != previous_time:
                throughput.append(8 * DataProcessor.get_average(aux) / 10)
                aux = []

        return throughput

    @staticmethod
    def get_packet_delivery_ratio(tx_packets, rx_packets, time):
        time_stamps = DataProcessor.get_time_stamps(time)
        pdr = []
        aux_tx = []
        aux_rx = []

        for (previous_time, current_time, value_tx, value_rx) \
                in zip(time_stamps, time_stamps[1:], tx_packets, rx_packets):
            aux_tx.append(value_tx)
            aux_rx.append(value_rx)
            if current_time != previous_time:
                # Percentage of packets delivered
                pdr.append(len(aux_rx) / len(aux_tx) * 100)
                aux_tx = []
                aux_rx = []

        return pdr

    @staticmethod
    def get_not_attacked_packets(data):
        """
        Separates the not-attacked packets from the
        attacked ones.

        Context: The dataset by SOUSA et al. (2023)
        has 2 classes for specifying if a packet has
        been attacked or not. This method separates
        the information by said class.

        """
        not_attacked = []
        time = []

        for is_attack, delay, time_values in zip(data['isAttack'], data['delay'], data['time']):
            if is_attack == 0:
                not_attacked.append(delay)
                time.append(time_values)

        return not_attacked, time

    @staticmethod
    def convert_time_to_set(time):
        return list(set(time))[:-1]