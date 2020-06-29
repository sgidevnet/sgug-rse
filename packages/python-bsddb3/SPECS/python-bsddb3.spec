# Allow building with multiple Python versions in EPEL
%{?el7:%bcond_without python3_other}

# Metadata for Python-related macros (i.e. %%pypi_source)
## Upstream package/project name
%global srcname bsddb3

## Description common to all version-specific subpackages
%global common_description %{expand:
This package contains Python wrappers for Berkeley DB, the Open Source embedded
database system. The Python wrappers allow you to store Python string objects of
any length.}

Name:           python-%{srcname}
Version:        6.2.6
Release:        10%{?dist}
Summary:        Python 3 bindings for Berkeley DB

License:        BSD
URL:            https://pypi.org/project/bsddb3
Source0:        %{pypi_source}

Patch:          bsddb3-collections-abc.patch

BuildRequires:  gcc libdb-devel

%description    %{common_description}


# Mainline Python 3 subpackage
%global python3_name        %{expand:python%{python3_pkgversion}-%{srcname}}
%package -n     %{python3_name}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide %{python3_name}}

%description -n %{python3_name} %{common_description}


# Alternative Python 3 subpackage
%if %{with python3_other}
%global python3_other_name  %{expand:python%{python3_other_pkgversion}-%{srcname}}
%package -n     %{python3_other_name}
Summary:        %{summary}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%{?python_provide:%python_provide %{python3_other_name}}

%description -n %{python3_other_name} %{common_description}
%endif


%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%{py3_build}
%{?with_python3_other:%py3_other_build}

%install
# Helper installation functions
fix_scripts_shebangs_and_permissions() {
    local -r py_binary="$1"
    local -r py_install_dir="$2"

    local -r WRONG_SHEBANG='#!/usr/bin/python|#!/usr/bin/env python[[:digit:]]*'
    local -r CORRECT_SHEBANG="#!${py_binary}"

    # Fix shebangs
    grep --recursive --files-with-matches --null --extended-regexp \
        --regexp="${WRONG_SHEBANG}" "${py_install_dir}" \
    | xargs --null -- sed --regexp-extended --in-place \
        --expression="s@${WRONG_SHEBANG}@${CORRECT_SHEBANG}@"

    # Set correct permissions on scripts
    grep --recursive --files-with-matches --null --extended-regexp \
        --regexp="${CORRECT_SHEBANG}" "${py_install_dir}" \
    | xargs --null -- chmod 0755

    # Recompile bytecode for changed files
    %{py_byte_compile "${py_binary}" "${py_install_dir}"}
}

# Latter builds override former ones
%if %{with python3_other}
%py3_other_install
fix_scripts_shebangs_and_permissions %{__python3_other} \
    %{buildroot}%{python3_other_sitearch}/%{srcname}
%endif

%{py3_install}
fix_scripts_shebangs_and_permissions %{__python3} \
    %{buildroot}%{python3_sitearch}/%{srcname}

# Get rid of unneeded header
rm -f %{buildroot}%{_includedir}/python3.*/%{srcname}/bsddb.h


%check
%{__python3} test.py
%{?with_python3_other:%{__python3_other} test.py}

%files -n %{python3_name}
%doc ChangeLog PKG-INFO README.txt
%license LICENSE.txt
%{python3_sitearch}/bsddb3/
%{python3_sitearch}/bsddb3-%{version}-py%{python3_version}.egg-info

%if %{with python3_other}
%files -n %{python3_other_name}
%doc ChangeLog PKG-INFO README.txt
%license LICENSE.txt
%{python3_other_sitearch}/bsddb3/
%{python3_other_sitearch}/bsddb3-%{version}-py%{python3_other_version}.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.2.6-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jan Staněk <jstanek@redhat.com> - 6.2.6-8
- Add patch for import compatibility with Python 3.9

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2.6-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2.6-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Jan Staněk <jstanek@redhat.com> - 6.2.6-3
- Restructure and rename package in order to enable EPEL builds

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Jan Staněk <jstanek@redhat.com> - 6.2.6-1
- Update to 6.2.6 (https://www.jcea.es/programacion/pybsddb.htm#bsddb3-6.2.6)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.2.5-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Jan Staněk <jstanek@redhat.com> - 6.2.5-3
- Apply the shebang fix to the right files.

* Tue Oct 10 2017 Jan Staněk <jstanek@redhat.com> - 6.2.5-2
- Fix generic python shebangs (https://pagure.io/packaging-committee/issue/698)

* Wed Oct 04 2017 Jan Stanek <jstanek@redhat.com> - 6.2.5-1
- Update to 6.2.5 (https://www.jcea.es/programacion/pybsddb.htm#bsddb3-6.2.5)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Jan Stanek <jstanek@redhat.com> - 6.2.4-1
- Update to version 6.2.4 (https://www.jcea.es/programacion/pybsddb.htm#bsddb3-6.2.4)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 6.2.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 05 2016 Jan Stanek <jstanek@redhat.com> - 6.2.0-1
- Update to version 6.2.0 (https://www.jcea.es/programacion/pybsddb.htm#bsddb3-6.2.0)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Jan Stanek <jstanek@redhat.com> - 6.1.1-1
- Update to version 6.1.1 (https://www.jcea.es/programacion/pybsddb.htm#bsddb3-6.1.1)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Dec 06 2013 Jan Stanek <jstanek@redhat.com> - 6.0.1-1
- Update to 6.0.1

* Mon Sep 23 2013 Jan Stanek <jstanek@redhat.com> - 6.0.0-1
- Initial package
