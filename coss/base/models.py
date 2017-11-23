class CossBaseModel(object):

    def get_featured(self):
        """Return the first Page<type> that has a featured attribute."""

        stack = [self]
        nodes = []
        while stack:
            current_node = stack.pop()
            nodes.append(current_node)
            for page_obj in current_node.get_children():
                stack.insert(0, page_obj)
                if hasattr(page_obj.specific, 'featured') and page_obj.specific.featured:
                    # If there is return two random results and stop looking deeper in the tree
                    return page_obj.specific_class.objects.filter(featured=True).order_by('?')[:2]
        return self.specific_class.objects.none()
