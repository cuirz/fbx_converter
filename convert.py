import os
import fbx


def export(file_name):
    print 'Converting [%s] to binary file' % file_name
    # Create an SDK manager
    manager = fbx.FbxManager.Create()
    # Create a scene
    scene = fbx.FbxScene.Create(manager, "")
    # Create an importer object
    importer = fbx.FbxImporter.Create(manager, "")
    # Specify the path and name of the file to be imported
    importstat = importer.Initialize(file_name, -1)
    if not importstat:
        print "not support file [%s]" % file_name
        return
    if not importer.Import(scene):
        print "Could not import this file for scene.[%s]" % file_name
        return
    # Create an exporter object
    exporter = fbx.FbxExporter.Create(manager, "")
    file_name = file_name[0:file_name.rindex('.')]
    save_path = "out/%s.fbx" % file_name
    if not os.path.isdir('out'):
        os.mkdir('out')
    # Specify the path and name of the file to be imported
    exportstat = exporter.Initialize(save_path, -1)
    exportstat = exporter.Export(scene)
    exporter.Destroy()
    importer.Destroy()
    scene.Destroy()
    manager.Destroy()


if __name__ == '__main__':
    ext_files = ['.fbx', '.obj']
    _list = os.listdir('.')
    for f in _list:
        if os.path.isfile(f):
            _texts = os.path.splitext(f.lower())
            if len(_texts) > 1 and _texts[1] in ext_files:
                export(f)
