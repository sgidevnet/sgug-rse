Name:           python-olefile
Version:        0.46
Release:        11%{?dist}
Summary:        Python package to parse, read and write Microsoft OLE2 files

%global         srcname         olefile
%global         _description    %{expand:
olefile is a Python package to parse, read and write Microsoft OLE2 files
(also called Structured Storage, Compound File Binary Format or Compound
Document File Format), such as Microsoft Office 97-2003 documents,
vbaProject.bin in MS Office 2007+ files, Image Composer and FlashPix files,
Outlook messages, StickyNotes, several Microscopy file formats, McAfee
antivirus quarantine files, etc.
}

# Build with python3 package by default
%bcond_without  python3

# Build without python2 package for newer releases > fc32 and > rhel8
# python2 package already released for rhel8
# https://pagure.io/fesco/issue/2266
%if (0%{?fedora} && 0%{?fedora} > 33 ) || ( 0%{?rhel} && 0%{?rhel} > 8 ) || 0%{?flatpak}
%bcond_with     python2
%else
%bcond_without  python2
%endif


License:        BSD
URL:            https://www.decalage.info/python/olefile
#               https://pypi.python.org/pypi/olefile/
#               https://github.com/decalage2/olefile/releases
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.zip

BuildArch:      noarch
BuildRequires:  dos2unix
BuildRequires:  /usr/bin/find

%description %{_description}

%package doc
Summary:        %{summary}
BuildArch:      noarch
# Fedora >= 31 does not have python2-sphinx anymore.
# There is python-sphinx in RHEL 7, but it's possibly too old.
# Python26 sphinx works
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme

%description doc %{_description}
This package contains documentation for %{name}.



%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}
Python2 version.
%endif



%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
#BuildRequires:  python%%{python3_pkgversion}-sphinx_rtd_theme
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python3 version.
%endif



%prep
%autosetup -p1 -n %{srcname}-%{version}

# Fix windows EOL
find ./ -type f -name '*.py' -exec dos2unix '{}' ';'
dos2unix doc/*.rst


%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

make -C doc html BUILDDIR=_doc_build SPHINXBUILD=sphinx-build-%{python3_version}



%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%py3_install
%endif



%check
# Tests got left out in the 0.44 source archive
# https://github.com/decalage2/olefile/issues/56
%if 0%{?with_python2}
PYTHONPATH=%{buildroot}%{python2_sitelib} %{__python2} tests/test_olefile.py
%endif

%if 0%{?with_python3}
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} tests/test_olefile.py
%endif


%files doc
%doc doc/_doc_build/html


%if 0%{?with_python2}
%files -n python2-%{srcname}
%doc README.md
%license doc/License.rst
%{python2_sitelib}/olefile-*.egg-info
%{python2_sitelib}/olefile/
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%license doc/License.rst
%{python3_sitelib}/olefile-*.egg-info
%{python3_sitelib}/olefile/
%endif


%changelog
* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 0.46-11
- Build python2 subpackage on F33, python2-pillow is still around

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.46-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Michal Ambroz <rebus AT_ seznam.cz> - 0.46-8
- rebuild for new version of oletools
- conditional stop building python2 subpackage on fc>32 and rhel>8
- split doc to separate subpackage

* Mon Oct 07 2019 Sandro Mani <manisandro@gmail.com> - 0.46-7
- BR: python-setuptools (#1758972)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.46-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.46-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Sandro Mani <manisandro@gmail.com> - 0.46-3
- Drop docs in python2 build

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Sandro Mani <manisandro@gmail.com> - 0.46-1
- Update to 0.46

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 0.45.1-2
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Sandro Mani <manisandro@gmail.com> - 0.45.1-1
- Update to 0.45.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Robert Scheck <robert@fedoraproject.org> - 0.44-4
- Added spec file conditionals to build for EPEL 7 (#1498616)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Sandro Mani <manisandro@gmail.com> - 0.44-1
- Update to 0.44

* Mon Jan 02 2017 Sandro Mani <manisandro@gmail.com> - 0.44-0.4.gitbc9d196
- Fix incorrect line endings
- Remove shebang from non-executable scripts

* Mon Jan 02 2017 Sandro Mani <manisandro@gmail.com> - 0.44-0.3.gitbc9d196
- Further reduce duplicate text
- Add python_provides

* Mon Jan 02 2017 Sandro Mani <manisandro@gmail.com> - 0.44-0.2.gitbc9d196
- Use %%py_build and %%py_install macros
- Use %%summary, %%url to reduce duplicate text
- Add %%check
- Move BR to subpackages

* Mon Jan 02 2017 Sandro Mani <manisandro@gmail.com> - 0.44-0.1.gitbc9d196
- Initial package
