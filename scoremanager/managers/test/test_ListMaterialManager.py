# -*- encoding: utf-8 -*-
import os
import shutil
from abjad import *
import scoremanager


def test_ListMaterialManager_01():

    score_manager = scoremanager.core.ScoreManager()
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.abjad_material_packages_directory_path,
        'testlist',
        )
    directory_entries = [
        '__init__.py', 
        '__metadata__.py',
        'output_material.py',
        ]
    input_ = 'lmm nmm list testlist 17 foo done b default q'

    assert not os.path.exists(path)
    try:
        score_manager._run(pending_user_input=input_, is_test=True)
        assert os.path.exists(path)
        manager = scoremanager.managers.ListMaterialManager(path)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_material_module()
        assert output_material == [17, 'foo']
        input_ = 'lmm testlist rm remove q'
        score_manager._run(pending_user_input=input_, is_test=True)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)
