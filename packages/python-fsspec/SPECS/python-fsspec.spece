# Avoid fsspec -> distributed -> dask -> fsspec dependency loop.
%bcond_without bootstrap

%global srcname fsspec

Name:           python-%{srcname}
Version:        0.7.4
Release:        2%{?dist}
Summary:        Specification for Pythonic file system interfaces

License:        BSD
URL:            https://github.com/intake/filesystem_spec
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
%if %{fedora} < 32
BuildRequires:  python3dist(pyftpdlib)
%endif
%if %{without bootstrap}
BuildRequires:  python3dist(distributed)
%endif
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(cloudpickle)
# Won't work in a build since it requires the kernel module to be loaded.
#BuildRequires:  python3dist(fusepy)
# Requires a running SSH server in a container.
#BuildRequires:  python3dist(paramiko)

%global _description %{expand:
Filesystem Spec is a project to unify various projects and classes to work with
remote filesystems and file-system-like abstractions using a standard pythonic
interface.}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n filesystem_spec-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{python3} -m pytest -vra -k 'not test_strip_protocol_expanduser'


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-2
- Rebuilt for Python 3.9

* Wed May 20 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.4-1
- Update to latest version

* Thu Apr 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.3-1
- Update to latest version

* Wed Apr 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-1
- Update to latest version

* Fri Mar 27 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-1
- Update to latest version

* Sun Mar 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.2-1
- Update to latest version

* Fri Nov 29 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.1-1
- Update to latest version

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.0-1
- Update to latest version

* Thu Oct 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.2-1
- Update to latest version

* Sat Sep 28 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.1-1
- Update to latest version

* Thu Sep 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.4-1
- Initial package.
