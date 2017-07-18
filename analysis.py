from nibabel import nb

nii = nb.load("mni_template.nii.gz")

print(nii.header)
