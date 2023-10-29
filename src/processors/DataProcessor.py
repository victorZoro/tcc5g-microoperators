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
        return time.astype(int)

    @staticmethod
    def get_average(data):
        return sum(data) / len(data)

    @staticmethod
    def get_avg_by_second(data, time):
        time_stamps = DataProcessor.get_time_stamps(time)
        average = []
        aux = []

        for (previous_time, current_Time, value) in zip(time_stamps, time_stamps[1:], data):
            aux.append(value)
            if current_Time != previous_time:
                average.append(DataProcessor.get_average(aux))
                aux = []

        return average

    @staticmethod
    def get_throughput(data, time):
        time_stamps = DataProcessor.get_time_stamps(time)
        throughput = []
        aux = []

        for (previous_time, current_Time, value) in zip(time_stamps, time_stamps[1:], data):
            aux.append(value)
            if current_Time != previous_time:
                print(8 * DataProcessor.get_average(aux))
                throughput.append(8 * DataProcessor.get_average(aux) * 4000 / 1e6)
                aux = []

        return throughput
