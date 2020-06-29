# Created by pyp2rpm-3.3.2
%global pypi_name apply-defaults

%global _description %{expand:
Apply default values to functions. Application settings come from a config
file into your code cleanly.
}

Name:           python-%{pypi_name}
Version:        0.1.4
Release:        4%{?dist}
Summary:        Helps pull configuration into a project

License:        MIT
URL:            https://github.com/bcb/apply_defaults
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/apply_defaults-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_description

%prep
%autosetup -n apply_defaults-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/apply_defaults/
%{python3_sitelib}/apply_defaults-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.4-2
- Fix issues pointed out during review

* Sun Dec 22 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.1.4-1
- Initial package.
