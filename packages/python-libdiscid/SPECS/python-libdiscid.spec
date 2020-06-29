Name:           python-libdiscid
Version:        0.4.1
Release:        24%{?dist}
Summary:        Python bindings for libdiscid

License:        MIT
URL:            http://pythonhosted.org/python-libdiscid/
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch0:         https://github.com/sebastinas/python-libdiscid/commit/91955e9.patch

BuildRequires:  gcc
BuildRequires:  libdiscid-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-Cython >= 0.15

%description
python-libdiscid provides Python bindings for libdiscid. libdiscid's
main purpose is the calculation of identifiers for audio discs to use
for the MusicBrainz database.

%package     -n python%{python3_pkgversion}-libdiscid
Summary:        Python 3 bindings for libdiscid
%{?python_provide:%python_provide python%{python3_pkgversion}-libdiscid}

%description -n python%{python3_pkgversion}-libdiscid
python%{python3_pkgversion}-libdiscid provides Python 3 bindings for libdiscid. libdiscid's
main purpose is the calculation of identifiers for audio discs to use
for the MusicBrainz database.


%prep
%autosetup -p1
rm libdiscid/_discid.c  # rebuilt with system Cython

# Fix sys.path for docs build
sed -i "s|os.path.join('../', b.build_lib)|'../build/lib.%{python3_platform}-%{python3_version}'|" docs/conf.py


%build
%py3_build
%{__python3} setup.py build_sphinx
rm build/html/.buildinfo


%install
%py3_install


%check
%{__python3} -Wall setup.py test


%files -n python%{python3_pkgversion}-libdiscid
%license LICENSE
%doc changelog PKG-INFO build/html/
%{python3_sitearch}/*libdiscid*/
%exclude %{python3_sitearch}/*libdiscid*/tests/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-18
- Subpackage python2-libdiscid has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.1-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Matěj Cepl <mcepl@redhat.com> - 0.4.1-11
- All req. pkgs are in EPEL7, we can built python3 packages as well.

* Fri May 26 2017 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-10
- Run tests with -Wall

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov  4 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-5
- Apply upstream fix for Cython >= 0.23

* Thu Aug  6 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-4
- Spec cleanup per current Python guidelines; Python 2 package is now python2-*

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-2
- Build below source dir instead of in %%{py3dir}

* Thu Mar  5 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-1
- First build
