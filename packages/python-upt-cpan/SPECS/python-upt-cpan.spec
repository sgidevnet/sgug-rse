%bcond_with tests # requires internet access

%global srcname upt-cpan

Name: python-upt-cpan  
Version: 0.5
Release: 4%{?dist}
Summary: CPAN front-end for upt

License: BSD
URL: https://framagit.org/upt/upt-cpan
Source0: %pypi_source
BuildArch: noarch

%description
CPAN front-end for upt.

%package -n python%{python3_pkgversion}-%{srcname}
Summary: CPAN front-end for upt
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-requests-mock
%if %{with tests}
BuildRequires: upt
%endif

%description -n python%{python3_pkgversion}-%{srcname}
CPAN front-end for upt.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m unittest
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md CHANGELOG
%license LICENSE
%{python3_sitelib}/upt_cpan-*.egg-info/
%{python3_sitelib}/upt_cpan/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Jeremy Bertozzi <jeremy.bertozzi@gmail.com> - 0.5-2
- Remove 'requires' tags

* Sun Sep 29 2019 Jeremy Bertozzi <jeremy.bertozzi@gmail.com> - 0.5-1
- Initial package
