%{?python_enable_dependency_generator}

%global modname sqlacodegen

Name:           python-%{modname}
Version:        2.0.0
Release:        9%{?dist}
Summary:        Automatic model code generator for SQLAlchemy

License:        MIT
URL:            https://github.com/agronholm/sqlacodegen
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{modname}; echo ${n:0:1})/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
This is a tool that reads the structure of an existing database and generates\
the appropriate SQLAlchemy model code, using the declarative style if possible.\
\
This tool was written as a replacement for sqlautocode, which was suffering\
from several issues (including, but not limited to, incompatibility with\
Python 3 and the latest SQLAlchemy version).\
\
Features:\
* Supports SQLAlchemy 0.8.x - 1.2.x\
* Produces declarative code that almost looks like it was hand written\
* Produces PEP 8 compliant code\
* Accurately determines relationships, including many-to-many, one-to-one\
* Automatically detects joined table inheritance\
* Excellent test coverage

%description %{_description}

%package -n python3-%{modname}
Summary:        Automatic model code generator for SQLAlchemy
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools >= 36.2.7
BuildRequires:  python3-setuptools_scm >= 1.7.0

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

#check
# Requires multiple DBs to be running

%files -n python3-%{modname}
%license LICENSE
%doc README.rst CHANGES.rst
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-3
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-9
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.6-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-4
- Rebuild for Python 3.6

* Sun Feb 14 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.6-3
- Fixup building after bug in python-pytest-cache

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.6-1
- Initial package
