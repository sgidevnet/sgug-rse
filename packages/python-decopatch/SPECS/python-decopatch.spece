Name:		python-decopatch
Version:	1.4.6
Release:	3%{?dist}
Summary:	A helper to write python decorators

License:	BSD
URL:		https://pypi.org/project/decopatch
Source0:	%{pypi_source decopatch}

BuildArch:	noarch
BuildRequires:	pyproject-rpm-macros

%global _description %{expand:
Because of a tiny oddity in the python language, writing decorators
without help can be a pain because you have to handle the
no-parenthesis usage explicitly. decopatch provides a simple way to
solve this issue so that writing decorators is simple and
straightforward.}

%description %_description

%package -n python3-decopatch
Summary: %{summary}
%{?python_provide:%python_provide python3-decopatch}

%description -n python3-decopatch %_description

%prep
%autosetup -n decopatch-%{version}
cat >pyproject.toml <<EOF
[build-system]
requires = ["pytest-runner", "setuptools_scm", "pypandoc", "six", "wheel"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc',?//" setup.py
sed -r -i '/^pandoc$/d' ci_tools/requirements-pip.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# Tests require pytest-cases, which requires this package. Yay!
%{__python3} -m pytest -v || :

%files -n python3-decopatch
%license LICENSE
%doc README.md
%{python3_sitelib}/decopatch/
%{python3_sitelib}/decopatch-%{version}.dist-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.6-1
- Initial packaging
