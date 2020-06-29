%global pypi_name PyMuPDF

Name:           python-%{pypi_name}
Version:        1.17.2
Release:        1%{?dist}
Summary:        Python binding for MuPDF - a lightweight PDF and XPS viewer

# PyMuPDF itself is GPLv3+.  MuPDF (statically linked) is AGPLv3+.
License:        GPLv3+ and AGPLv3+
URL:            https://github.com/pymupdf/PyMuPDF
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# Can be removed if mupdf provides a shared library
Patch0:         fix-library-linking.patch

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  gcc
BuildRequires:  swig
BuildRequires:  zlib-devel
BuildRequires:  mupdf-static
# Can be removed if mupdf provides a shared library
BuildRequires:  libjpeg-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  jbig2dec-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel

%global _description %{expand:
This is PyMuPDF, a Python binding for MuPDF - a lightweight PDF and XPS
viewer.  MuPDF can access files in PDF, XPS, OpenXPS, epub, comic and fiction
book formats, and it is known for its top performance and high rendering
quality.  With PyMuPDF you therefore can also access files with extensions
*.pdf, *.xps, *.oxps, *.epub, *.cbz or *.fb2 from your Python scripts.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%package        doc
Summary:        Documentation for python-%{pypi_name}
BuildArch:      noarch

%description    doc
python-%{pypi_name}-doc contains documentation and examples for PyMuPDF

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
sphinx-build docs docs_built

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} \
  %{__python3} -c 'import sys; sys.path.remove(""); import fitz'


%files -n python3-%{pypi_name}
%license COPYING "GNU AFFERO GPL V3"
%{python3_sitearch}/fitz/
%{python3_sitearch}/PyMuPDF*

%files doc
%doc demo docs_built/* README.md

%changelog
* Fri Jun 26 2020 Scott Talbert <swt@techie.net> - 1.17.2-1
- Update to new upstream release 1.17.2 (#1850817)

* Thu Jun 18 2020 Scott Talbert <swt@techie.net> - 1.17.1-1
- Update to new upstream release 1.17.1 (#1848770)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Michael J Gruber <mjg@fedoraproject.org> - 1.17.0-1
- Update to new upstream release 1.17.0 (#1838287)

* Mon May 04 2020 Scott Talbert <swt@techie.net> - 1.16.18-1
- Update to new upstream release 1.16.18 (#1822800)

* Sun Mar 29 2020 Scott Talbert <swt@techie.net> - 1.16.16-1
- Update to new upstream release 1.16.16 (#1818610)

* Thu Mar 26 2020 Scott Talbert <swt@techie.net> - 1.16.14-1
- Update to new upstream release 1.16.14 (#1817211)

* Wed Mar 18 2020 Scott Talbert <swt@techie.net> - 1.16.13-1
- Update to new upstream release 1.16.13 (#1814049)

* Fri Mar 13 2020 Scott Talbert <swt@techie.net> - 1.16.12-1
- Update to new upstream release 1.16.12 (#1812963)

* Tue Feb 25 2020 Scott Talbert <swt@techie.net> - 1.16.11-1
- Update to new upstream release 1.16.11 (#1806372)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Scott Talbert <swt@techie.net> - 1.16.10-1
- Update to new upstream release 1.16.10 (#1785875)

* Thu Dec 12 2019 Scott Talbert <swt@techie.net> - 1.16.9-1
- Update to new upstream release 1.16.9 (#1773810)

* Tue Nov 12 2019 Scott Talbert <swt@techie.net> - 1.16.7-1
- Update to new upstream release 1.16.7 (#1771130)

* Thu Nov 07 2019 Scott Talbert <swt@techie.net> - 1.16.6-1
- Update to new upstream release 1.16.6 (#1768266)

* Tue Oct 15 2019 Scott Talbert <swt@techie.net> - 1.16.5-1
- Update to new upstream release 1.16.5 (#1761164)

* Sat Sep 14 2019 Scott Talbert <swt@techie.net> - 1.16.2-1
- Update to new upstream release 1.16.2 (#1751945)

* Wed Sep 04 2019 Scott Talbert <swt@techie.net> - 1.16.1-1
- Update to new upstream release 1.16.1 (#1747043)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.14.20-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Scott Talbert <swt@techie.net> - 1.14.20-1
- Update to new upstream release 1.14.20 (#1742123)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Scott Talbert <swt@techie.net> - 1.14.17-1
- Update to new upstream release 1.14.17 (#1727474)

* Thu Jun 13 2019 Scott Talbert <swt@techie.net> - 1.14.16-1
- Update to new upstream release 1.14.16 (#1713110)

* Wed Jun 12 2019 Scott Talbert <swt@techie.net> - 1.14.14-3
- Temporarily build our own copy of mupdf to fix FTBFS (#1716518)

* Tue May 07 2019 Scott Talbert <swt@techie.net> - 1.14.14-2
- Restore linking with harfbuzz (#1706753)

* Thu Apr 18 2019 Scott Talbert <swt@techie.net> - 1.14.14-1
- New upstream release 1.14.14

* Mon Apr 08 2019 Scott Talbert <swt@techie.net> - 1.14.13-1
- New upstream release 1.14.13

* Fri Mar 22 2019 Scott Talbert <swt@techie.net> - 1.14.12-1
- New upstream release 1.14.12

* Tue Mar 12 2019 Scott Talbert <swt@techie.net> - 1.14.10-1
- New upstream release 1.14.10

* Fri Mar 08 2019 Scott Talbert <swt@techie.net> - 1.14.9-1
- New upstream release 1.14.9

* Thu Jan 31 2019 Scott Talbert <swt@techie.net> - 1.14.8-1
- New upstream release 1.14.8

* Fri Jan 25 2019 Scott Talbert <swt@techie.net> - 1.14.7-1
- New upstream release 1.14.7

* Tue Nov 20 2018 Scott Talbert <swt@techie.net> - 1.14.1-1
- New upstream release 1.14.1

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.13.20-2
- Subpackage python2-PyMuPDF has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Sep 14 2018 Scott Talbert <swt@techie.net> - 1.13.20-1
- New upstream release 1.13.20

* Sat Aug 04 2018 Scott Talbert <swt@techie.net> - 1.13.16-1
- New upstream release 1.13.16

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.13.15-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Scott Talbert <swt@techie.net> - 1.13.15-1
- New upstream release 1.13.15

* Fri Jul 20 2018 Scott Talbert <swt@techie.net> - 1.13.14-1
- New upstream release 1.13.14

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Scott Talbert <swt@techie.net> - 1.13.13-1
- New upstream release 1.13.13

* Wed Jun 27 2018 Scott Talbert <swt@techie.net> - 1.13.12-1
- New upstream release 1.13.12

* Tue Jun 26 2018 Scott Talbert <swt@techie.net> - 1.13.11-1
- New upstream release 1.13.11

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.13.10-2
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Scott Talbert <swt@techie.net> - 1.13.10-1
- New upstream release 1.13.10

* Sun Jun 10 2018 Scott Talbert <swt@techie.net> - 1.13.9-1
- Initial package.
