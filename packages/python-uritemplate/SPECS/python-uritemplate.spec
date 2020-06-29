%global modname uritemplate
%global altname uritemplate.py

%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        3.0.1
Release:        2%{?dist}
Summary:        Simple python library to deal with URI Templates (RFC 6570)

License:        BSD or ASL 2.0
URL:            https://%{modname}.readthedocs.io
Source0:        https://github.com/sigmavirus24/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
Conflicts:      python3-uri-templates
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{altname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n uritemplate-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v

%files -n python3-%{modname}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc HISTORY.rst README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-2
- Rebuilt for Python 3.9

* Sun May 03 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.0.1-1
- update to 3.0.1
- declare licensing correctly and include actual license files

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0.0-10
- Don't test on EL-8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-8
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-7
- Subpackage python2-uritemplate has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Nick Bebout <nb@fedoraproject.org> - 3.0.0-1
- Upgrade to 3.0.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.0-1
- Initial package
