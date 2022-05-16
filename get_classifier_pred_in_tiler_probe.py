while l_obj is not None:
    try:
        # Casting l_obj.data to pyds.NvDsObjectMeta
        obj_meta = pyds.NvDsObjectMeta.cast(l_obj.data) 
        l_class = obj_meta.classifier_meta_list
        # while l_class is not None:

        while l_class is not None:
            try:
                class_meta = pyds.NvDsClassifierMeta.cast(l_class.data)
            except StopIteration:
                break

            l_label = class_meta.label_info_list

            while l_label is not None:
                try:
                    label_info = pyds.NvDsLabelInfo.cast(l_label.data)
                except StopIteration:
                    break

                print(label_info.result_label)

                try:
                    l_label=l_label.next
                except StopIteration:
                    break
            try:
                l_class=l_class.next
            except StopIteration:
                break
    except StopIteration:
        break
