"""

    This example shows creating and modification of structures using portpy
"""

import portpy as pp


def eg_3_structure_transformations():
    # Enter patient name
    patient_name = 'Lung_Patient_1'

    # visualize patient metadata for beams_dict and structures
    pp.Visualize.display_patient_metadata(patient_name)

    # display patients
    pp.Visualize.display_patients()

    # create my_plan object for the planner beams_dict
    # for the customized beams_dict, you can pass the argument beam_ids
    # e.g. my_plan = Plan(patient_name, beam_ids=[0,1,2,3,4,5,6], options=options)
    my_plan = pp.Plan(patient_name)

    # boolean or create margin_mm around structures
    my_plan.structures.union(str_1='PTV', str_2='GTV', str1_or_str2='dummy')
    my_plan.structures.intersect(str_1='PTV', str_2='GTV', str1_and_str2='dummy')
    my_plan.structures.subtract(str_1='PTV', str_2='GTV', str1_sub_str2='dummy')
    my_plan.structures.expand(structure='PTV', margin_mm=5, new_structure='dummy')


if __name__ == "__main__":
    eg_3_structure_transformations()