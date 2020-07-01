%{?python_enable_dependency_generator}

%global modname prov

Name:           python-%{modname}
Version:        1.5.2
Release:        9%{?dist}
Summary:        W3C Provenance Data Model supporting PROV-JSON and PROV-XML import/export

License:        MIT
URL:            https://pypi.python.org/pypi/prov
Source0:        https://github.com/trungdong/prov/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
A library for W3C Provenance Data Model supporting PROV-JSON and PROV-XML\
import/export.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{_bindir}/%{modname}-*
%{python3_sitelib}/%{modname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.2-3
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Thu Jun 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.5.0-5
- use python2- prefix

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Require and BuildRequire python3-rdflib >= 4.2.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuild for Python 3.6

* Thu Oct 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-1
- Initial package
