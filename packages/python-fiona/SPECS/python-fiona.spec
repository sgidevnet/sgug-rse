%global srcname fiona
%global Srcname Fiona

Name:           python-%{srcname}
Version:        1.8.13
#global         pre rc1
%global         uversion %{version}%{?pre}
Release:        5%{?dist}
Summary:        Fiona reads and writes spatial data files

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/Toblerity/%{Srcname}/archive/%{uversion}/%{Srcname}-%{uversion}.tar.gz

# Adapt test for gdal-3.1.0
# https://github.com/Toblerity/Fiona/commit/02a1f39165abef2e138cdb0f39cb289a11cf79b2#diff-2341932de631b9528511ad91757d523a
Patch0:         fiona_tests.patch

BuildRequires:  gcc-c++
BuildRequires:  gdal >= 1.8
BuildRequires:  gdal-devel >= 1.8

%{?python_enable_dependency_generator}

%description
Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python types
and protocols such as files, dictionaries, mappings, and iterators instead of
classes specific to OGR. Fiona can read and write real-world data using
multi-layered GIS formats and zipped virtual file systems and integrates
readily with other Python GIS packages such as pyproj, Rtree, and Shapely.


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-attrs >= 17
BuildRequires:  python3-click >= 4.0
BuildRequires:  python3-click-plugins >= 1.0
BuildRequires:  python3-cligj >= 0.5
BuildRequires:  python3-munch
BuildRequires:  python3-six >= 1.7
BuildRequires:  python3-boto3 >= 1.2.4
BuildRequires:  python3-shapely

BuildRequires:  python3-pytest

Recommends:     python3-boto3
Recommends:     python3-shapely

%description -n python3-%{srcname}
Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python types
and protocols such as files, dictionaries, mappings, and iterators instead of
classes specific to OGR. Fiona can read and write real-world data using
multi-layered GIS formats and zipped virtual file systems and integrates
readily with other Python GIS packages such as pyproj, Rtree, and Shapely.


%prep
%autosetup -n %{Srcname}-%{uversion} -p1


%build
%py3_build


%install
%py3_install


%check
export LANG=C.UTF-8

rm -rf fiona  # Needed to not load the unbuilt library.

# Skip debian tests since we are not on debian
PYTHONPATH="%{buildroot}%{python3_sitearch}" \
    %{__python3} -m pytest -m "not network and not wheel" -k "not debian" -ra


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst CHANGES.txt CREDITS.txt
%{_bindir}/fio
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{Srcname}-%{uversion}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.13-5
- Rebuilt for Python 3.9

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 1.8.13-4
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.8.13-3
- Rebuild (gdal)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.13-1
- Update to latest version

* Tue Nov 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.11-1
- Update to latest version

* Mon Oct 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.9-3
- Update to latest version

* Sun Sep 29 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.8-3
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.6-1
- Update to latest version

* Sat Mar 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.5-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.4-1
- Update to 1.8.4

* Thu Nov 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Sun Oct 28 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8-0.3.rc1
- Update to 1.8rc1

* Sat Sep 22 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8-0.2.a2
- Drop Python 2 subpackage

* Fri Sep 21 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8-0.1.a2
- Update to 1.8a2
- Use automatic Python dependency generator
- Use pytest instead of nose

* Wed Jul 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.13-1
- Update to latest version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.10-4
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.10-3
- rebuilt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.7.10-1
- Update to latest version.
- Use python2-* BR.

* Sun Jul 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.7.8-2
- Restore flaky test patch (not applied upstream yet)

* Sun Jul 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.7.8-1
- Simplify spec a bit.
- Update fiona to latest release.

* Sun Mar 05 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.7.4-3
- Fix flaky ls test.

* Sun Mar 05 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.7.4-2
- Testing requires pytest as well.

* Sat Mar 04 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.7.4-1
- Initial package release.
