%global srcname geopandas

Name:           python-%{srcname}
Version:        0.7.0
Release:        2%{?dist}
Summary:        Geographic Pandas extensions
%global _description \
GeoPandas is a project to add support for geographic data to Pandas objects. \
\
The goal of GeoPandas is to make working with geospatial data in Python easier. \
It combines the capabilities of Pandas and Shapely, providing geospatial \
operations in Pandas and a high-level interface to multiple geometries to \
Shapely. GeoPandas enables you to easily do operations in Python that would \
otherwise require a spatial database such as PostGIS.

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/%{srcname}/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch0001:      0001-Skip-test_overlay_nybb-on-broken-platforms.patch

BuildArch:      noarch

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-descartes
BuildRequires:  python3-fiona >= 1.0.1
BuildRequires:  python3-pandas >= 0.23
BuildRequires:  python3-pyproj >= 2.2
BuildRequires:  python3-shapely >= 1.2.18

BuildRequires:  python3-pytest
BuildRequires:  python3-rtree >= 0.8
BuildRequires:  python3-matplotlib >= 2.0.1

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    py.test-%{python3_version} -ra geopandas -m 'not web'


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-1
- Update to latest version

* Sat Feb 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.0-1
- Update to latest version

* Sat Aug 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.0-0.1.rc1
- Update to latest release candidate

* Sat Aug 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.1-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-1
- Update to latest version

* Sat Mar 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-2
- Drop Python 2 subpackage

* Wed Jul 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-6
- Add patch to build against Pandas 0.23.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-6
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-5
- rebuilt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-3
- Add patch for non-x86 systems.
- Use python2-* BR.

* Fri Dec 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-2
- Add patch for non-x86 systems.

* Tue Sep 19 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version.
- Use lowercase rtree dependency.
- Fix inconsistent capitalization.

* Sat Aug 12 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-3
- Simplify spec with more macros.

* Sun Jul 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-2
- Simplify spec a bit.
- Add patch for new Pandas compatibility.

* Sun Mar 05 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Initial package release.
