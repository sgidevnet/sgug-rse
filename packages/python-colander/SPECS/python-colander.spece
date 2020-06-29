%{?python_enable_dependency_generator}
%global modname colander

Name:           python-%{modname}
Version:        1.7.0
Release:        6%{?dist}
Summary:        Simple schema-based serialization and deserialization library

License:        BSD
URL:            https://pypi.python.org/pypi/colander
Source0:        https://github.com/Pylons/colander/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
An extensible package which can be used to:\
\
- deserialize and validate a data structure composed of strings, mappings,\
  and lists.\
- serialize an arbitrary data structure to a data structure composed of\
  strings, mappings, and lists.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-coverage
BuildRequires:  python3-translationstring
BuildRequires:  python3-iso8601

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -p1 -n %{modname}-%{version}

# The presence of this file creates an rpmlint error.  Remove it.
rm docs/.gitignore
rm -rf docs/.static

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{modname}
%license LICENSE.txt COPYRIGHT.txt
%doc README.rst CONTRIBUTORS.txt CHANGES.rst docs
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-*.egg-info/

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-1
- Update to 1.7.0 Fixes bug #1632024
- Fixes CVE-2017-18361

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4-7
- Enable python dependency generator

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-6
- Subpackage python2-colander has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.4-2
- Include the locale/ folder (#1527683).

* Sat Sep 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4-1
- Update to 1.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 27 2017 Kevin Fenzi <kevin@scrye.com> - 1.3.3-1
- Update to 1.3.3. Fixes bug #1445275

* Sat Feb 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
