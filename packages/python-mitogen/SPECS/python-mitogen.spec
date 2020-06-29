# what it's called on pypi
%global srcname mitogen
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Mitogen is a Python library for writing distributed self-replicating programs.

There is no requirement for installing packages, copying files around, writing
shell snippets, upfront configuration, or providing any secondary link to a
remote machine aside from an SSH connection. Due to its origins for use in
managing potentially damaged infrastructure, the remote machine need not even
have free disk space or a writeable filesystem.

It is not intended as a generic RPC framework; the goal is to provide a robust
and efficient low-level API on which tools like Salt, Ansible, or Fabric can be
built, and while the API is quite friendly and comparable to Fabric, ultimately
it is not intended for direct use by consumer software.

The focus is to centralize and perfect the intricate dance required to run
Python code safely and efficiently on a remote machine, while avoiding
temporary files or large chunks of error-prone shell scripts, and supporting
common privilege escalation techniques like sudo, potentially in combination
with exotic connection methods such as WMI, telnet, or console-over-IPMI.}


%if (%{defined fedora} && 0%{?fedora} < 30) || (%{defined rhel} && 0%{?rhel} < 8)
%bcond_without  python2
%endif

%if %{defined fedora} || (%{defined rhel} && 0%{?rhel} >= 8)
%bcond_without  python3
%endif


Name:           python-%{pkgname}
Version:        0.2.9
Release:        3%{?dist}
Summary:        Distributed self-replicating programs in Python
License:        BSD
URL:            https://github.com/dw/mitogen
Source0:        %pypi_source
# Mitogen jumps through some hoops for Python 2.4 support.  We don't need that in
# Fedora or EPEL.  Part of that is bundled compatibility libraries.  This patch
# removes the methods that stuff those compat libraries into the PYTHONPATH.  You
# should also delete the mitogen/compat and ansible_mitogen/compat directories.
Patch0:         remove-compat.patch
BuildArch:      noarch


%description %{common_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{common_description}
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}
%endif


%prep
%autosetup -n %{srcname}-%{version} -p 1

rm -rf %{eggname}.egg-info

# See patch0 comment above
rm -r mitogen/compat ansible_mitogen/compat


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}


%check
# tests/README.md says the tests need:
#    - internet connection
#    - working docker daemon


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{libname}
%{python2_sitelib}/ansible_%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{libname}
%{python3_sitelib}/ansible_%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Carl George <carl@george.computer> - 0.2.9-1
- Latest upstream

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.8-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Carl George <carl@george.computer> - 0.2.8-1
- Latest upstream

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Carl George <carl@george.computer> - 0.2.6-2
- Improve patch0

* Tue Apr 16 2019 Carl George <carl@george.computer> - 0.2.6-1
- Latest upstream

* Thu Feb 14 2019 Carl George <carl@george.computer> - 0.2.5-1
- Latest upstream

* Tue Feb 12 2019 Carl George <carl@george.computer> - 0.2.4-1
- Initial package
