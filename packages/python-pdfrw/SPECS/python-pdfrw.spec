
%global srcname pdfrw

Name: python-%{srcname}
Version: 0.4
Release: 11%{?dist}
Summary: Python library to read and write PDF files
License: MIT

URL:     https://github.com/pmaupin/pdfrw
Source0: %{pypi_source}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildArch: noarch

%description
pdfrw is a Python library and utility that reads and writes PDF files. pdfrw
can also be used in conjunction with reportlab, in order to re-use portions
of existing PDFs in new PDFs created with reportlab.


%package -n python3-%{srcname}
Summary: Python library to read and write PDF files
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
pdfrw is a Python library and utility that reads and writes PDF files. pdfrw
can also be used in conjunction with reportlab, in order to re-use portions
of existing PDFs in new PDFs created with reportlab.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc README.rst examples
%{python3_sitelib}/*

%changelog
* Thu Jun 25 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 0.4-11
- add python3-setuptools to BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 0.4-8
- remove "python2-pdfrw" subpackage

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Felix Schwarz <fschwarz@fedoraproject.org> - 0.4-1
- New upstream version (0.4)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Sergio Pascual <sergiopr at fedoraproject.org> - 0.3-1
- New upstream version (0.3)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Sergio Pascual <sergiopr at fedoraproject.org> - 0.2-2
- New 0.2 version with Python3 support, using new macros
- Yes, I forgot to upload the tarball

* Sun Nov 15 2015 Till Maas <opensource@till.name> - 0.1-6
- Use %%license

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 0.1-2
- Cleaned line removing buildroot in install
- Including examples in docs

* Tue Apr 30 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 0.1-1
- New spec file
