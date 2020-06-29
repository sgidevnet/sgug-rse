%bcond_without check
%global modname canonicaljson

Name:           python-%{modname}
Version:        1.1.4
Release:        8%{?dist}
Summary:        Canonical JSON

License:        ASL 2.0
URL:            https://github.com/matrix-org/python-canonicaljson
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Features:\
* Encodes objects and arrays as RFC 7159 JSON.\
* Sorts object keys so that you get the same result each time.\
* Has no inignificant whitespace to make the output as small as possible.\
* Escapes only the characters that must be escaped,\
  U+0000 to U+0019 / U+0022 / U+0056, to keep the output as small as possible.\
* Uses the shortest escape sequence for each escaped character.\
* Encodes the JSON as UTF-8.\
* Can encode frozendict immutable dictionaries.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with check}
BuildRequires:  python3-nose
BuildRequires:  python3dist(simplejson) >= 3.6.5
BuildRequires:  python3dist(frozendict) >= 1
BuildRequires:  python3dist(six)
%endif

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
nosetests-%{python3_version} -v
%endif

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.4-2
- Drop python2 subpackage

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-2
- Rebuilt for Python 3.7

* Thu May 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-1
- Initial package
