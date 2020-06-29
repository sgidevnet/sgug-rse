%{?python_enable_dependency_generator}
%global srcname geoplot

%bcond_with network

Name:           python-%{srcname}
Version:        0.4.1
Release:        2%{?dist}
Summary:        High-level geospatial plotting for Python

License:        MIT
URL:            https://github.com/ResidentMario/geoplot
# PyPI tarball does not include tests.
Source0:        https://github.com/ResidentMario/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
 
%global _description \
geoplot is a high-level Python geospatial plotting library. It's an extension \
to cartopy and matplotlib which makes mapping easy: like seaborn for \
geospatial.

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cartopy)
BuildRequires:  python3dist(contextily) >= 1
BuildRequires:  python3dist(descartes)
BuildRequires:  python3dist(geopandas)
BuildRequires:  python3dist(mapclassify) >= 2.1
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(mercantile)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mpl)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(seaborn)

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
# Skip tests that use the network.
PYTHONPATH=%{buildroot}%{python3_sitelib} MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 \
%if %{with network}
    pytest-3 tests/*tests.py
%else
    pytest-3 tests/*tests.py -k 'not webmap'
%endif


%files -n python3-%{srcname}
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-1
- Update to latest version

* Fri May 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-2
- Fix contextily dependency (#1830383)

* Sat Feb 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-2
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-2
- Enable python dependency generator

* Sun Jan 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version

* Mon Jul 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-2
- Enable all tests

* Sun Jul 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- Initial package.
