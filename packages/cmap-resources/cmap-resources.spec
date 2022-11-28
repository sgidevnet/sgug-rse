%global gittag 20180719

Name:           cmap-resources

# For legacy reasons, there are periods in the version number.
# It'd be nice to write some fancy macro to put them there!
Version:        2018.07.19

Release:        3%{?dist}
Summary:        CMap Resources for Adobe's public character collections

License:        BSD
URL:            https://github.com/adobe-type-tools/cmap-resources/
Source0:        https://github.com/adobe-type-tools/cmap-resources/archive/%{gittag}/cmap-resources-%{version}.zip

BuildRequires:  unzip

BuildArch:      noarch

%description
CMap (Character Map) resources are used to unidirectionally
map character codes, such as a Unicode encoding form, to CIDs
(Characters IDs, meaning glyphs) of a CIDFont resource.

%package cns1-7

Summary:       Traditional Chinese Adobe CMap resources

Obsoletes:     cmap-resources-cns1-6 < 2018.05.15-1

Requires:      %{name} = %{version}-%{release}

%description cns1-7
CMap (Character Map) resources are used to unidirectionally
map character codes, such as a Unicode encoding form, to CIDs
(Characters IDs, meaning glyphs) of a CIDFont resource.

This package contains the Traditional Chinese CMap resources.

%package gb1-5

Summary:       Simplified Chinese Adobe CMap resources

Requires:      %{name} = %{version}-%{release}

%description gb1-5
CMap (Character Map) resources are used to unidirectionally
map character codes, such as a Unicode encoding form, to CIDs
(Characters IDs, meaning glyphs) of a CIDFont resource.

This package contains the Traditional Chinese CMap resources.

%package japan2-0

Summary:       Japanese Adobe CMap resources

Requires:      %{name} = %{version}-%{release}

%description japan2-0
CMap (Character Map) resources are used to unidirectionally
map character codes, such as a Unicode encoding form, to CIDs
(Characters IDs, meaning glyphs) of a CIDFont resource.

This package contains Japanese CMap resources. They are
deprecated by Adobe but may still be needed. If you want the
current Japanese CMap resources, install the package
"cmap-resources-japan1-6".

%package japan1-6

Summary:       Japanese Adobe CMap resources

Requires:      %{name} = %{version}-%{release}

%description japan1-6
CMap (Character Map) resources are used to unidirectionally
map character codes, such as a Unicode encoding form, to CIDs
(Characters IDs, meaning glyphs) of a CIDFont resource.

This package contains the Japanese CMap resources.

%package korea1-2
Summary:       Korean Adobe CMap resources

Requires:      %{name} = %{version}-%{release}

%description korea1-2
CMap (Character Map) resources are used to unidirectionally
map character codes, such as a Unicode encoding form, to CIDs
(Characters IDs, meaning glyphs) of a CIDFont resource.

This package contains the Korean CMap resources.

%package identity-0
Summary:       Traditional Chinese Adobe CMap resources

Requires:      %{name} = %{version}-%{release}

%description identity-0
CMap (Character Map) resources are used to unidirectionally
map character codes, such as a Unicode encoding form, to CIDs
(Characters IDs, meaning glyphs) of a CIDFont resource.

This package contains the special purpose CMap resources.

%package kr-9
Summary:       Korean Adobe CMap resources

Requires:      %{name} = %{version}-%{release}

%description kr-9
CMap (Character Map) resources are used to unidirectionally
map character codes, such as a Unicode encoding form, to CIDs
(Characters IDs, meaning glyphs) of a CIDFont resource.

This package contains Korean Chinese CMap resources.

%prep
%setup -qn cmap-resources-%{gittag}

# Put the "deprecated" japan2-0 resources in the root directory.
# (We may as well ship them).
mv -v deprecated/* ./
rm -rv deprecated/

%build
# There is nothing to build.

%install
# Create a directory for the CMAP resources.
mkdir -p %{buildroot}%{_datadir}/cmap/

# Copy them all over.
cp -pr */ %{buildroot}%{_datadir}/cmap/

# Create symbolic links, since Adobe changed the naming convention again.
ln -s %{_datadir}/cmap/Adobe-CNS1-7 %{buildroot}%{_datadir}/cmap/cmap-cns1-7
ln -s %{_datadir}/cmap/Adobe-GB1-5 %{buildroot}%{_datadir}/cmap/cmap-gb1-5
ln -s %{_datadir}/cmap/Adobe-Korea1-2 %{buildroot}%{_datadir}/cmap/cmap-korea1-2
ln -s %{_datadir}/cmap/Adobe-KR-9 %{buildroot}%{_datadir}/cmap/cmap-kr-9
ln -s %{_datadir}/cmap/Adobe-Identity-0 %{buildroot}%{_datadir}/cmap/cmap-identity-0
ln -s %{_datadir}/cmap/Adobe-Japan1-6 %{buildroot}%{_datadir}/cmap/cmap-japan1-6
ln -s %{_datadir}/cmap/Adobe-Japan2-0 %{buildroot}%{_datadir}/cmap/cmap-japan2-0

%files
%dir %{_datadir}/cmap/
%doc README.md VERSIONS.txt
%license LICENSE.txt

%files cns1-7
%{_datadir}/cmap/Adobe-CNS1-7
%{_datadir}/cmap/cmap-cns1-7

%files gb1-5
%{_datadir}/cmap/Adobe-GB1-5
%{_datadir}/cmap/cmap-gb1-5

%files korea1-2
%{_datadir}/cmap/Adobe-Korea1-2
%{_datadir}/cmap/cmap-korea1-2

%files kr-9
%{_datadir}/cmap/Adobe-KR-9
%{_datadir}/cmap/cmap-kr-9

%files identity-0
%{_datadir}/cmap/Adobe-Identity-0
%{_datadir}/cmap/cmap-identity-0

%files japan1-6
%{_datadir}/cmap/Adobe-Japan1-6
%{_datadir}/cmap/cmap-japan1-6

%files japan2-0
%{_datadir}/cmap/Adobe-Japan2-0
%{_datadir}/cmap/cmap-japan2-0

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.07.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.07.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 Ben Rosser <rosser.bjr@gmail.com> - 2018.07.19-1
- Updated to latest upstream release.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.05.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Ben Rosser <rosser.bjr@gmail.com> - 2018.05.15-1
- Updated to latest upstream release (rhbz#1487835).
- Upstream renamed their resource directories; update and provide symlinks.
- Remove old Obsolete tags for the individual resource subpackages.
- Add new cmap-kr-9 subpackage.
- Deprecate cmap-cns1-6 package in favor of cmap-cns1-7, with appropriate obsolete.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct  1 2016 Ben Rosser <rosser.bjr@gmail.com> - 2016.09.04-2
- Remove bogus isa dep in cns1-6 on main package.

* Tue Sep  6 2016 Ben Rosser <rosser.bjr@gmail.com> - 2016.09.04-1
- Update to latest resources.
- Fix packaging error in cmap-resources-gb1-5.

* Fri Aug 19 2016 Ben Rosser <rosser.bjr@gmail.com> - 2015.12.05-2
- Fixed Source0 to include the project name in the download.
- Moved directory ownership, docs, and license file to main package.

* Sat Jun 25 2016 Ben Rosser <rosser.bjr@gmail.com> - 2015.12.05-1
- Initial repackage, now that upstream doesn't distribute separate archives.
- Rename korean1-2 to korea1-2 and identity0 to identity-0 as per upstream.
- Provide compatibility symlinks to the old versioned directories.
- Included actual documentation (README.txt, VERSIONS.txt) with each package.
- Upstream has changed the license _back_ to BSD.
