#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: 5424026
#
Name     : pypi-tornado
Version  : 6.4.2
Release  : 103
URL      : https://files.pythonhosted.org/packages/59/45/a0daf161f7d6f36c3ea5fc0c2de619746cc3dd4c76402e9db545bd920f63/tornado-6.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/59/45/a0daf161f7d6f36c3ea5fc0c2de619746cc3dd4c76402e9db545bd920f63/tornado-6.4.2.tar.gz
Summary  : Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-tornado-license = %{version}-%{release}
Requires: pypi-tornado-python = %{version}-%{release}
Requires: pypi-tornado-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(alabaster)
BuildRequires : pypi(babel)
BuildRequires : pypi(black)
BuildRequires : pypi(build)
BuildRequires : pypi(cachetools)
BuildRequires : pypi(certifi)
BuildRequires : pypi(chardet)
BuildRequires : pypi(charset_normalizer)
BuildRequires : pypi(click)
BuildRequires : pypi(colorama)
BuildRequires : pypi(distlib)
BuildRequires : pypi(docutils)
BuildRequires : pypi(filelock)
BuildRequires : pypi(flake8)
BuildRequires : pypi(idna)
BuildRequires : pypi(imagesize)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(mccabe)
BuildRequires : pypi(mypy)
BuildRequires : pypi(mypy_extensions)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pathspec)
BuildRequires : pypi(pip_tools)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(pluggy)
BuildRequires : pypi(py)
BuildRequires : pypi(pycodestyle)
BuildRequires : pypi(pyflakes)
BuildRequires : pypi(pygments)
BuildRequires : pypi(pyproject_api)
BuildRequires : pypi(pyproject_hooks)
BuildRequires : pypi(pytz)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(snowballstemmer)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinx_rtd_theme)
BuildRequires : pypi(sphinxcontrib_applehelp)
BuildRequires : pypi(sphinxcontrib_asyncio)
BuildRequires : pypi(sphinxcontrib_devhelp)
BuildRequires : pypi(sphinxcontrib_htmlhelp)
BuildRequires : pypi(sphinxcontrib_jsmath)
BuildRequires : pypi(sphinxcontrib_qthelp)
BuildRequires : pypi(sphinxcontrib_serializinghtml)
BuildRequires : pypi(tox)
BuildRequires : pypi(types_pycurl)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(virtualenv)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Tornado Web Server
==================
.. image:: https://badges.gitter.im/Join%20Chat.svg
:alt: Join the chat at https://gitter.im/tornadoweb/tornado
:target: https://gitter.im/tornadoweb/tornado?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

%package license
Summary: license components for the pypi-tornado package.
Group: Default

%description license
license components for the pypi-tornado package.


%package python
Summary: python components for the pypi-tornado package.
Group: Default
Requires: pypi-tornado-python3 = %{version}-%{release}

%description python
python components for the pypi-tornado package.


%package python3
Summary: python3 components for the pypi-tornado package.
Group: Default
Requires: python3-core
Provides: pypi(tornado)
Requires: pypi(alabaster)
Requires: pypi(babel)
Requires: pypi(black)
Requires: pypi(build)
Requires: pypi(cachetools)
Requires: pypi(certifi)
Requires: pypi(chardet)
Requires: pypi(charset_normalizer)
Requires: pypi(click)
Requires: pypi(colorama)
Requires: pypi(distlib)
Requires: pypi(docutils)
Requires: pypi(filelock)
Requires: pypi(flake8)
Requires: pypi(idna)
Requires: pypi(imagesize)
Requires: pypi(jinja2)
Requires: pypi(markupsafe)
Requires: pypi(mccabe)
Requires: pypi(mypy)
Requires: pypi(mypy_extensions)
Requires: pypi(packaging)
Requires: pypi(pathspec)
Requires: pypi(pip_tools)
Requires: pypi(platformdirs)
Requires: pypi(pluggy)
Requires: pypi(pycodestyle)
Requires: pypi(pyflakes)
Requires: pypi(pygments)
Requires: pypi(pyproject_api)
Requires: pypi(pyproject_hooks)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(snowballstemmer)
Requires: pypi(sphinx)
Requires: pypi(sphinx_rtd_theme)
Requires: pypi(sphinxcontrib_applehelp)
Requires: pypi(sphinxcontrib_asyncio)
Requires: pypi(sphinxcontrib_devhelp)
Requires: pypi(sphinxcontrib_htmlhelp)
Requires: pypi(sphinxcontrib_jsmath)
Requires: pypi(sphinxcontrib_qthelp)
Requires: pypi(sphinxcontrib_serializinghtml)
Requires: pypi(tox)
Requires: pypi(types_pycurl)
Requires: pypi(typing_extensions)
Requires: pypi(urllib3)
Requires: pypi(virtualenv)

%description python3
python3 components for the pypi-tornado package.


%prep
%setup -q -n tornado-6.4.2
cd %{_builddir}/tornado-6.4.2
pushd ..
cp -a tornado-6.4.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732288786
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tornado
cp %{_builddir}/tornado-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tornado/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tornado/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
