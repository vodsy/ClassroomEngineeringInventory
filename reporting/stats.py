from .models import ReportingData
from collections import Counter, defaultdict





class Model_Brand_Frequency_Bar():
    #Abstracted with many methods to ensure updates with page refresh
    def get_data(self):
        values_dict = {}
        for row in ReportingData.objects.all():
            model_brand = row.model_brand
            if row.model_brand not in values_dict:
                values_dict[model_brand] = 1
            else:
                values_dict[model_brand] += 1

        return values_dict

    def make_x_data_list(self):
        x_data = list(Model_Brand_Frequency_Bar.get_data(self).keys())

        return x_data

    def make_y_data_list(self):
        y_data = []
        for val in Model_Brand_Frequency_Bar.make_x_data_list(self):
            y_data.append(Model_Brand_Frequency_Bar.get_data(self)[val])

        return y_data


    def get_x_data(self):
        return Model_Brand_Frequency_Bar.make_x_data_list(self)

    def get_x_labels(self):
        x_labels = ""
        for label in Model_Brand_Frequency_Bar.get_x_data(self):
            x_labels += ("|" + str(label))
        x_labels = x_labels.replace(" ", "+")
        return x_labels

    def get_y_data(self):
        return Model_Brand_Frequency_Bar.make_y_data_list(self)


class Reason_Pie_Chart():
    #Abstracted with many methods to ensure updates with page refresh
    def get_data(self):
        values_dict = {}
        for row in ReportingData.objects.all():
            reason = row.get_reason_display()
            if row.get_reason_display() not in values_dict:
                values_dict[reason] = 1
            else:
                values_dict[reason] += 1

        return values_dict

    def make_x_data_list(self):
        x_data = list(Reason_Pie_Chart.get_data(self).keys())

        return x_data

    def make_y_data_list(self):
        y_data = []
        for val in Reason_Pie_Chart.make_x_data_list(self):
            y_data.append(Reason_Pie_Chart.get_data(self)[val])

        return y_data


    def get_x_data(self):
        return Reason_Pie_Chart.make_x_data_list(self)

    def get_x_labels(self):
        x_labels = ""
        for label in Reason_Pie_Chart.get_x_data(self):
            x_labels += (str(label) + "|")
        x_labels = x_labels.replace(" ", "+")
        return x_labels

    def get_y_data(self):
        return Reason_Pie_Chart.make_y_data_list(self)

    def get_y_labels(self):
        y_labels = ""
        for label in Reason_Pie_Chart.get_y_data(self):
            y_labels += (str(label) + "|")
        y_labels = y_labels.replace(" ", "+")
        return y_labels

#Use grouped bar chart
#get rid of choices
#show all equipment types
class Equipment_Stats():
    def get_data(self):
        values_dict = {}
        master_dict = {}
        for row in ReportingData.objects.all():

            model_brand = row.model_brand
            equipment = row.get_equipment_display()

            if equipment not in master_dict:
                master_dict[equipment] = {}
                master_dict[equipment][model_brand] = 1
            else:
                if model_brand not in master_dict[equipment]:
                    master_dict[equipment][model_brand] = 1
                else:
                    master_dict[equipment][model_brand] += 1

        return master_dict

    def make_x_labels(self):
        master_dict = Equipment_Stats.get_data(self)
        master_keys = master_dict.values()
        x_labels = ""

        for i in master_dict:
            x_labels += ("|" + str(i))

        x_labels = x_labels.replace(" ", "+")

        return x_labels


    def make_x_data(self):
        master_dict = Equipment_Stats.get_data(self)
        master_keys = master_dict.values()
        x_data = ""

        for i in master_keys:
            #x_data.append('|')
            for k in i:
                x_data += ("|" + str(k))
        x_data = x_data.replace(" ", "+")

        return x_data

    def make_y_data_list(self):
        master_dict = Equipment_Stats.get_data(self)
        master_keys = master_dict.values()
        y_data = ""

        for i in master_keys:
            for k in i.values():
                y_data += (str(k) + ",")
            y_data = y_data[:-1] + "|"

        if y_data[-1] == "|":
            y_data = y_data[:-1]


        return y_data

    def get_x_data(self):
        return Equipment_Stats.make_x_data(self)

    def get_x_labels(self):
        return Equipment_Stats.make_x_labels(self)

    def get_y_data(self):
        return Equipment_Stats.make_y_data_list(self)
