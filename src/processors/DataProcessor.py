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
        print(time_stamps)
        throughput = []
        sum = 0

        for (previous_time, current_time, value) in zip(time_stamps, time_stamps[1:], data):
            sum += value
            if current_time != previous_time:
                throughput.append(8 * sum / 1e6)
                sum = 0

        return throughput
