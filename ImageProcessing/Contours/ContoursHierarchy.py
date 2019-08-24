# %% [markdown] Background
# This is the explaination of an argument of cv.findContours()
#
# the argument is Contour Retrieval Mode
#
# And this function get three output
#
# the thrid one is Hierarchy
#
# What does it mean?

# %% [markdown] Hierarchy
# ## Key Word 1: Hierarchy
# ### Representation of contours' relationship is called the Hierarchy.

# ## Key Word 2: Presentation
# ### [Next, Previous, First_Child, Parent]
# %% [markdown] Contour Retrieval Mode
# ## RETR_LIST： without parent-child relationship
# ## RETR_EXTERNAL： only care about hierarchy-0
# ## RETR_CCOMP: rearrange contours to a 2-level hierarchy
# ## RETR_TREE: Mr.Perfect