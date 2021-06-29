%global luv Lüv

Name: luv-icon-theme
Summary: Flat, but complex, icon theme
License: CC-BY-SA

%global git_date    20200623
%global git_commit  42387fe9b7cc8c5766c8e46795598af7ee842369
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:8})

Version: 0.4.9.31
Release: 2.%{git_date}git%{git_commit_short}%{?dist}

URL: https://github.com/Nitrux/%{name}
Source0: %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

BuildArch: noarch

Requires: hicolor-icon-theme
Suggests: luv-wallpapers


%description
%{luv} is the spiritual successor to Flattr, a flat but complex icon theme.


%package -n luv-wallpapers
Summary: Wallpapers to accompany the %{luv} icon theme
BuildArch: noarch

%global paper_count 6

%description -n luv-wallpapers
A set of %{paper_count} different wallpapers to use alongside the %{luv} icon theme.


%prep
%autosetup -n %{name}-%{git_commit}

# Remove extra permission bits found on some files
find Luv/ -executable -type f -exec chmod --verbose a-x '{}' ';'

# Remove "dummy" directories
for DUMMY in $(find Luv/ -name 'dummy.txt'); do
	DUMMY_DIR="$(dirname "${DUMMY}")"
	rm "${DUMMY}"

	# Not doing rm -rf on the dir so we don't remove anything by mistake
	rmdir "${DUMMY_DIR}"
done


%build
# Nothing to do here


%install
# -- icons
ICON_DIR="%{buildroot}%{_datadir}/icons"
install -m 755 -d "${ICON_DIR}"
cp -a Luv/ "${ICON_DIR}/"

rm "${ICON_DIR}/Luv/LICENSE"

# -- wallpapers
PAPER_DIR="%{buildroot}%{_datadir}/wallpapers"
install -m 755 -d "${PAPER_DIR}"
cp -a Wallpapers "${PAPER_DIR}/"
mv "${PAPER_DIR}/Wallpapers" "${PAPER_DIR}/Luv"


%check
PAPERS=$(find %{buildroot}%{_datadir}/wallpapers/Luv/ -mindepth 1 -maxdepth 1 -type d | wc -l)
if [[ "$PAPERS" -ne "%{paper_count}" ]]; then
	echo "Error: The luv-wallpapers package says there are %{paper_count} wallpapers, but ${PAPERS} were found" >&2
	exit 1
fi


%transfiletriggerin -- %{_datadir}/icons/Luv
gtk-update-icon-cache --force %{_datadir}/icons/Luv &>/dev/null || :


%files
%license Luv/LICENSE

%dir %{_datadir}/icons/Luv
%{_datadir}/icons/Luv/*/

%{_datadir}/icons/Luv/index.theme
%ghost %{_datadir}/icons/Luv/icon-theme.cache


%files -n luv-wallpapers
%license Luv/LICENSE
%{_datadir}/wallpapers/Luv


%changelog
* Tue Jun 23 2020 Artur Iwicki <fedora@svgames.pl> - 0.4.9.31-2.20200623git42387fe9
- Update to latest git snapshot
- Remove executable bits found on some files
- Don't install "dummy" directories
- Check if the actual wallpaper count matches what's in luv-wallpapers description

* Tue May 05 2020 Artur Iwicki <fedora@svgames.pl> - 0.4.9.31-1.20200504git6f0fb464
- Initial packaging
