import os
from experimental.tools.scoremanagertools.wranglers.AssetWrangler import AssetWrangler


class ImportableAssetWrangler(AssetWrangler):

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def temporary_asset_package_path(self):
        if self.current_asset_container_package_path:
            return self.dot_join([
                self.current_asset_container_package_path,
                self.temporary_asset_short_name])
        else:
            return self.temporary_asset_short_name

    ### PUBLIC METHODS ###

    def list_asset_package_paths(self, head=None):
        result = []
        result.extend(self.list_score_external_asset_package_paths(head=head))
        result.extend(self.list_score_internal_asset_package_paths(head=head))
        result.extend(self.list_user_asset_package_paths(head=head))
        return result

    def list_asset_proxies(self, head=None):
        result = []
        for package_path in self.list_asset_package_paths(head=head):
            asset_proxy = self.get_asset_proxy(package_path)
            result.append(asset_proxy)
        return result

    def list_score_external_asset_package_paths(self, head=None):
        result = []
        for path in self.list_score_external_asset_container_paths(head=head):
            for name in os.listdir(path):
                package_path = self.path_to_package_path(path)
                if name[0].isalpha():
                    result.append(self.dot_join([package_path, name]))
        return result

    def list_score_internal_asset_package_paths(self, head=None):
        result = []
        for asset_container_package_path in \
            self.list_score_internal_asset_container_package_paths(head=head):
            if self.score_internal_asset_container_package_path_infix:
                asset_path = self.package_path_to_directory_path(
                    asset_container_package_path)
                for name in os.listdir(asset_path):
                    if name[0].isalpha():
                        importable_base_name = self.strip_extension_from_base_name(name)
                        result.append('{}.{}'.format(
                            asset_container_package_path, importable_base_name))
            else:
                result.append(asset_container_package_path)
        return result

    def list_user_asset_package_paths(self, head=None):
        result = []
        for path in self.list_user_asset_container_paths(head=head):
            for name in os.listdir(path):
                if name[0].isalpha():
                    result.append(self.dot_join([self.configuration.user_makers_package_path, name]))
        return result

    # TODO: try to reimplement without proxy instantiation
    def list_visible_asset_package_paths(self, head=None):
        result = []
        for asset_proxy in self.list_visible_asset_proxies(head=head):
            result.append(asset_proxy.package_path)
        return result

    def make_visible_asset_menu_tokens(self, head=None):
        keys = self.list_visible_asset_package_paths(head=head)
        bodies = self.list_visible_asset_human_readable_names(head=head)
        return zip(keys, bodies)
