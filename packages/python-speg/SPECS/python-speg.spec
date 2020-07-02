%{?python_enable_dependency_generator}
%global py2support 0
%global srcname speg
%global commit 877acddfd5ac5ae8b4a4592d045e74e108477643
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0.3
Release:        9.git%{shortcommit}%{?dist}
Summary:        A PEG-based parser interpreter with memoization (in time)
License:        MIT
URL:            https://github.com/avakar/speg
Source0:        https://github.com/avakar/speg/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
A PEG-based parser interpreter with memoization.

%if %{py2support}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A PEG-based parser interpreter with memoization.
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A PEG-based parser interpreter with memoization.

%prep
%autosetup -n %{srcname}-%{commit}

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
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-9.git877acdd
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-7.git877acdd
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-6.git877acdd
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4.git877acdd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3-3.git877acdd
- Enable python dependency generator

* Thu Jan  3 2019 Tom Callaway <spot@fedoraproject.org> - 0.3-2.git877acdd
- disable py2support

* Wed Jan  2 2019 Tom Callaway <spot@fedoraproject.org> - 0.3-1.git877acdd
- new package

