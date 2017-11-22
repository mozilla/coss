class CossBaseModel(object):

    def get_featured(self):
        """Return the first Page<type> that has a featured attribute."""

        for page_obj in self.get_children():

            # Check if there is a featured field in the model in question
            if hasattr(page_obj.specific, 'featured'):
                # If there is return two random results and stop looking deeper in the tree
                return page_obj.specific_class.objects.filter(featured=True).order_by('?')[:2]
            page_obj.specific.get_featured()
