#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC24E631BABB1FE70 (jpakkane@gmail.com)
#
Name     : meson
Version  : 0.56.1
Release  : 69
URL      : https://github.com/mesonbuild/meson/releases/download/0.56.1/meson-0.56.1.tar.gz
Source0  : https://github.com/mesonbuild/meson/releases/download/0.56.1/meson-0.56.1.tar.gz
Source1  : https://github.com/mesonbuild/meson/releases/download/0.56.1/meson-0.56.1.tar.gz.asc
Summary  : A high performance build system
Group    : Development/Tools
License  : Apache-2.0
Requires: meson-bin = %{version}-%{release}
Requires: meson-data = %{version}-%{release}
Requires: meson-license = %{version}-%{release}
Requires: meson-man = %{version}-%{release}
Requires: meson-python = %{version}-%{release}
Requires: meson-python3 = %{version}-%{release}
Requires: ninja
Requires: tqdm
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : ninja
BuildRequires : tqdm

%description
ftdetect sets the filetype
ftplugin sets Meson indentation rules
indent does Meson indentation
syntax does Meson syntax highlighting

%package bin
Summary: bin components for the meson package.
Group: Binaries
Requires: meson-data = %{version}-%{release}
Requires: meson-license = %{version}-%{release}

%description bin
bin components for the meson package.


%package data
Summary: data components for the meson package.
Group: Data

%description data
data components for the meson package.


%package license
Summary: license components for the meson package.
Group: Default

%description license
license components for the meson package.


%package man
Summary: man components for the meson package.
Group: Default

%description man
man components for the meson package.


%package python
Summary: python components for the meson package.
Group: Default
Requires: meson-python3 = %{version}-%{release}

%description python
python components for the meson package.


%package python3
Summary: python3 components for the meson package.
Group: Default
Requires: python3-core
Provides: pypi(meson)

%description python3
python3 components for the meson package.


%prep
%setup -q -n meson-0.56.1
cd %{_builddir}/meson-0.56.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609958339
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/meson
cp %{_builddir}/meson-0.56.1/COPYING %{buildroot}/usr/share/package-licenses/meson/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
# install syntax highlight files for vim
install -dm 0755 %{buildroot}/usr/share/vim/vim82/{ftdetect,ftplugin,indent,syntax}
install -m0644 ./data/syntax-highlighting/vim/ftdetect/*   %{buildroot}/usr/share/vim/vim82/ftdetect/
install -m0644 ./data/syntax-highlighting/vim/ftplugin/*   %{buildroot}/usr/share/vim/vim82/ftplugin/
install -m0644 ./data/syntax-highlighting/vim/indent/*     %{buildroot}/usr/share/vim/vim82/indent/
install -m0644 ./data/syntax-highlighting/vim/syntax/*     %{buildroot}/usr/share/vim/vim82/syntax/
# syntax highlight for nvim
install -dm 0755 %{buildroot}/usr/share/nvim/runtime/{ftplugin,indent,syntax}
install -m0644 ./data/syntax-highlighting/vim/ftplugin/*   %{buildroot}/usr/share/nvim/runtime/ftplugin/
install -m0644 ./data/syntax-highlighting/vim/indent/*     %{buildroot}/usr/share/nvim/runtime/indent/
install -m0644 ./data/syntax-highlighting/vim/syntax/*     %{buildroot}/usr/share/nvim/runtime/syntax/
# syntax highlight for emacs
install -dm 0755 %{buildroot}/usr/share/emacs/site-lisp
install -m0644 ./data/syntax-highlighting/emacs/*          %{buildroot}/usr/share/emacs/site-lisp/
# shell completion for bash
install -dm 0755 %{buildroot}/usr/share/bash-completion/completions
install -m0644 ./data/shell-completions/bash/*             %{buildroot}/usr/share/bash-completion/completions/
# shell completions for zsh
install -dm 0755 %{buildroot}/usr/share/zsh/site-functions
install -m0644 ./data/shell-completions/zsh/*              %{buildroot}/usr/share/zsh/site-functions/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/meson

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/meson
/usr/share/emacs/site-lisp/meson.el
/usr/share/nvim/runtime/ftplugin/meson.vim
/usr/share/nvim/runtime/indent/meson.vim
/usr/share/nvim/runtime/syntax/meson.vim
/usr/share/polkit-1/actions/com.mesonbuild.install.policy
/usr/share/vim/vim82/ftdetect/meson.vim
/usr/share/vim/vim82/ftplugin/meson.vim
/usr/share/vim/vim82/indent/meson.vim
/usr/share/vim/vim82/syntax/meson.vim
/usr/share/zsh/site-functions/_meson

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/meson/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/meson.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
