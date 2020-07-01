%{?python_enable_dependency_generator}
%global py2support 0
%global srcname cson

Name:           python-%{srcname}
Version:        0.8
Release:        6%{?dist}
Summary:        A Coffescript Object Notation (CSON) parser for Python 2 and Python 3
License:        MIT
URL:            https://github.com/avakar/pycson
Source0:        https://github.com/avakar/pycson/archive/%{version}/pycson-%{version}.tar.gz
BuildArch:      noarch

%description
A python parser for the Coffeescript Object Notation (CSON).

%if %{py2support}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A python parser for the Coffeescript Object Notation (CSON).
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A python parser for the Coffeescript Object Notation (CSON).

%prep
%autosetup -n pycson-%{version}

%build
%if %{py2support}
%py2_build
%endif
%py3_build

%install
%if %{py2support}
%py2_install
%endif
%py3_install

# Note that there is no %%files section for the unversioned python module
%if %{py2support}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{srcname}/
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  9 2019 Tom Callaway <spot@fedoraproject.org> - 0.8-1
- update to 0.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7-3
- Enable python dependency generator

* Wed Jan  2 2019 Tom Callaway <spot@fedoraproject.org> - 0.7-2
- fix Source0

* Wed Jan  2 2019 Tom Callaway <spot@fedoraproject.org> - 0.7-1
- new package
