%global srcname pyPEG2

Name:		python3-%{srcname}
Version:	2.15.2
Release:	12%{?dist}
Summary:	A PEG Parser-Interpreter in Python
%{?python_provide:%python_provide python3-%{srcname}}

License:	GPLv2
URL:		http://fdik.org/pyPEG
Source0:	https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:  noarch
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
Requires: python3-lxml

%description
pyPEG is a plain and simple intrinsic parser interpreter framework for Python
version 3.x. It is based on Parsing Expression Grammar, PEG.
With pyPEG you can parse many formal languages in a very easy way.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build

%install
%py3_install


%check
PYTHONPATH=. py.test-%{python3_version} pypeg2/test


%files
%license LICENSE.txt
%doc README.txt CHANGES.txt PKG-INFO docs
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%{python3_sitelib}/pypeg2


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.15.2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 Tomas Orsava <torsava@redhat.com> - 2.15.2-7
- Rebuilding after Fedora 27 branched, try 2 due to broken tagging

* Wed Aug 16 2017 Tomas Orsava <torsava@redhat.com> - 2.15.2-6
- Rebuilding after Fedora 27 branched

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.15.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 16 2016 Tomas Orsava <torsava@redhat.com> - 2.15.2-1
- Let there be package.
- This package is needed as a dependency for qutebrowser.

