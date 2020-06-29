Name:		python-makefun
Version:	1.6.11
Release:	3%{?dist}
Summary:	Dynamically create python functions with a proper signature

License:	BSD
URL:		https://pypi.org/project/makefun
Source0:	%{pypi_source makefun}

BuildArch:	noarch
BuildRequires:	pyproject-rpm-macros

%global _description \
%summary.

%description %_description

%package -n python3-makefun
Summary: %{summary}
%{?python_provide:%python_provide python3-makefun}

%description -n python3-makefun %_description

%prep
%autosetup -n makefun-%{version}

cat >pyproject.toml <<EOF
[build-system]
requires = ["pytest-runner", "setuptools_scm", "pypandoc", "six", "wheel"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc', //" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# Tests require pytest-cases, which requires this package. Yay!
%{__python3} -m pytest -v || :

%files -n python3-makefun
%license LICENSE
%doc README.md
%{python3_sitelib}/makefun/
%{python3_sitelib}/makefun-%{version}.dist-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.11-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.11-1
- Initial packaging
