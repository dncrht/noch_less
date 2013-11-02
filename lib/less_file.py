# -*- coding: utf-8 -*-

class LessFile:

    def __init__(self, *args, **kwargs):
        """
        Decomposes a string into the relevant parts.
        Used as object parameter.
        Instance variables: id, source, destination
        """

        if args:
            filename = args[0]
            self.source = filename.strip().replace('file://',  '')

            source_parts = self.source.split('/')
            self.id = source_parts[-1].replace('.less', '')

            source_parts.pop()
            source_parts.pop() # destination directory is the upper of the source, so compilation doesn't trigger itself
            source_parts.append("%s.css" % self.id)
            self.destination = "/".join(source_parts)

        else: #assume kwargs
            self.id = kwargs['id']
            self.source = kwargs['source']
            self.destination = kwargs['destination']
